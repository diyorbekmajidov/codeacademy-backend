# Endpoints

## The Table of Contents

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `task/add/` | Add a new task |
| GET | `task/all/` | Get all tasks |
| POST | `task/update/<task_id>/` | Update a task |
| POST | `task/delete/<task_id>/` | Delete a task |
| POST | `assignment/add/` | Add a new assignment |
| GET | `assignment/all/` | Get all assignments |
| GET | `assignment/<assignment_id>/` | Get a assignment by id |
| POST | `assignment/update/<assignment_id>/` | Update a assignment |
| POST | `assignment/delete/<assignment_id>/` | Delete a assignment |
| POST | `add-tasks-to-assignment/<assignment_id>/` | Add tasks to an assignment |
| POST | `remove-tasks-from-assignment/<assignment_id>/` | Remove tasks from an assignment |
| GET | `get-tasks-from-assignment/<assignment_id>/` | Get tasks from an assignment |
| GET | `get-tasks-from-assignment/<assignment_id>/` | Get tasks from an assignment |
| POST | `result/` | get result by lesson and assignment id |

## The Endpoints Details

### GET `lesson/get/<group_id>/` - Get lessons by group id

#### API Request

```bash
curl -X GET {base url}/lesson/get/<group_id>/
```

#### API Response

```json
[
    {
        "id": 1,
        "name": "print",
        "description": "",
        "date_created": "2023-02-22T06:48:26.390177Z",
        "date_updated": "2023-02-22T06:48:26.390216Z",
        "group": 1,
        "assignments": [
            1,
            2,
            3,
        ]
    },
    {
        "id": 2,
        "name": "input",
        "description": "",
        "date_created": "2023-02-22T06:48:26.390177Z",
        "date_updated": "2023-02-22T06:48:26.390216Z",
        "group": 1,
        "assignments": [
            1,
            2,
            3,
        ]
    }
]
```

##### Response Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | `int` | The lesson's id |
| `name` | `string` | The lesson's name |
| `description` | `string` | The lesson's description |
| `date_created` | `string` | The lesson's date created |
| `date_updated` | `string` | The lesson's date updated |
| `group` | `int` | The lesson's group |
| `assignments` | `list` | The lesson's assignments |

### GET `lesson/assignment/<int:pk>/` - Get assignments by lesson id

#### API Request

```bash
curl -X GET {base url}/lesson/assignment/1/
```

#### API Response

```json
[
    {
        "id": 1,
        "name": "variables_and_types",
        "description": "",
        "course": 1,
        "link": "",
        "type": {
            "id": 1,
            "name": "homework",
            "date_created": "2023-02-20T09:49:11.990267Z",
            "date_updated": "2023-02-20T09:49:11.990313Z"
        },
        "date_created": "2023-02-20T10:06:05.321219Z",
        "date_updated": "2023-02-20T10:06:05.321258Z"
    },
    {
        "id": 2,
        "name": "variables_and_arithmetic_operators_homework",
        "description": "",
        "course": 1,
        "link": "",
        "type": {
            "id": 1,
            "name": "homework",
            "date_created": "2023-02-20T09:49:11.990267Z",
            "date_updated": "2023-02-20T09:49:11.990313Z"
        },
        "date_created": "2023-02-20T10:06:05.434480Z",
        "date_updated": "2023-02-20T10:06:05.434510Z"
    }
]
```

##### Response Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | `int` | The assignment's id |
| `name` | `string` | The assignment's name |
| `description` | `string` | The assignment's description |
| `course` | `int` | The assignment's course |
| `link` | `string` | The assignment's link |
| `type` | `object` | The assignment's type |
| `date_created` | `string` | The assignment's date created |
| `date_updated` | `string` | The assignment's date updated |

### POST `result/` - Get result by lesson and assignment id

#### API Request

```bash
curl -X POST {base url}/result/ -d '{"lesson": 1, "assignment": 1}'
```

#### API Response

```json
[
    {
        "student": "Ja'far Zokirov",
        "attempt": 0,
        "result": [
            {
                "id": 41,
                "name": "arithmetic_op01",
                "is_correct": false,
                "attempt": 0
            },
            {
                "id": 42,
                "name": "arithmetic_op02",
                "is_correct": false,
                "attempt": 0
            },
            {
                "id": 43,
                "name": "arithmetic_op03",
                "is_correct": false,
                "attempt": 0
            }
        ]
    },
    {
        "student": "Azizbek Raxmonberdiyev",
        "attempt": 0,
        "result": [
            {
                "id": 41,
                "name": "arithmetic_op01",
                "is_correct": false,
                "attempt": 0
            },
            {
                "id": 42,
                "name": "arithmetic_op02",
                "is_correct": false,
                "attempt": 0
            },
            {
                "id": 43,
                "name": "arithmetic_op03",
                "is_correct": false,
                "attempt": 0
            }
        ]
    }
```

##### Response Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `student` | `string` | The student's name |
| `attempt` | `int` | The student's attempt |
| `result` | `list` | The student's result |

###### `result` Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | `int` | The task's id |
| `name` | `string` | The task's name |
| `is_correct` | `bool` | The task's is solved |
| `attempt` | `int` | The task's attempt |
