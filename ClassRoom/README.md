# Endpoints

## The Table of Contents

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Returns a welcome message |
| POST | `/student/<student_id>/` | Returns a student's information |
| POST | `/student/add/` | Adds a student to the database |
| POST | `/student/update/<student_id>/` | Updates a student's information |
| POST | `/student/delete/<student_id>/` | Deletes a student from the database |
| GET | `/student/all/` | Returns all students in the database |
| GET | `/course/` | Returns all courses in the database |
| POST | `/course/add/` | Adds a course to the database |
| POST | `/course/update/<course_id>/` | Updates a course's information |
| POST | `/course/delete/<course_id>/` | Deletes a course from the database |
| GET | `/group/all/` | Returns all groups in the database |
| GET | `/group/<course_id>/` | Returns all groups in a course |
| POST | `/group/add/` | Adds a group to the database |
| POST | `/group/update/<group_id>/` | Updates a group's information |
| POST | `/group/delete/<group_id>/` | Deletes a group from the database |
| POST | `/add-students-to-group/<group_id>/` | Adds students to a group |
| POST | `/remove-students-from-group/<group_id>/` | Removes students from a group |
| GET | `/get-students-from-group/<group_id>/` | Returns all students in a group |

## The Endpoints Details

### GET `/course/all/` - Returns all courses in the database

#### API Request

```bash
curl -X GET `{base url}/course/`
```

#### API Response

```json
[
    {
        "id": 1,
        "name": "Python Foundation"
    },
    {
        "id": 2,
        "name": "Dart Foundation"
    }
]

```

##### Response Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | `int` | The course's id |
| `name` | `string` | The course's name |

### GET `group/<course_id>/` - Returns all groups in a course

#### API Request

```bash
curl -X GET {base url}/group/1/
```

#### API Response

```json
[
    {
        "id": 1,
        "name": "Python Foundation - Group 1"
    },
    {
        "id": 2,
        "name": "Python Foundation - Group 2"
    }
]

```

##### Response Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | `int` | The group's id |
| `name` | `string` | The group's name |
