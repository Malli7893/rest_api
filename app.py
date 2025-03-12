from flask import Flask , jsonify

todo = Flask(__name__)

students=[
{
    "id":1,
    "name":"abhi",
    "age": 20
},
    {
"id":2,
    "name":"abhi",
    "age": 20
    }
]


@todo.route('/student_list')
def get_students_list():
    return jsonify(students)
@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    print(id)
    for std in students:
        return jsonify(std)
    print(std)
    return "hello"

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )