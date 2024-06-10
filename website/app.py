from flask import Flask, render_template, request
import pickle
import linecache

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST','GET'])
def index():
    pred = 0

    if request.method == 'POST':
        types = request.form['types']
        qualification = request.form['qualification']
        qualification2 = request.form['qualification2']
        duration = request.form['duration']
        category = request.form['category']
        level = request.form['level']

        print(types,qualification,qualification2,duration,category,level)

        feature_list = []
        
        feature_list.append(int(duration))

        types_list = ['course', 'specializations', 'professional certificates','guided project', 'none']
        qualification_list = ['OL Passes 0', 'OL Passes 5', 'OL Passes 9']
        qualification2_list = ['AL Passes 0', 'AL Passes 3']
        category_list = ['Business Essentials', 'Cloud Computing','Computer Security and Networks', 'Data Analysis',
        'Design and Product','Environmental Science and Sustainability','Machine Learning', 'Math and Logic', 
        'Networking', 'Physics and Astronomy','Support and Operations', 'other_category']
        level_list = ['Advanced Level', 'Beginner Level', 'Intermediate Level', 'None']

        def traverse(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse(types_list, types)
        traverse(qualification_list, qualification)
        traverse(qualification2_list, qualification2)
        traverse(category_list, category)
        traverse(level_list, level)
        
        pred = prediction(feature_list)
        print(int(pred))

        # if int(pred) > 90:
        #     pred = 'Very good'
        # elif int(pred) > 80:
        #     pred = 'Good'
        # else:
        #     pred=pred

        # with open("course.txt", "r") as file:
        #     line = int(pred)
        #     pred = file.readline(line)
        # file.close()
        
        line= int(pred)

        pred = linecache.getline('course.txt', line)



    return render_template("index.html", pred = pred)
if __name__ == '__main__':
    app.run(debug=True)
