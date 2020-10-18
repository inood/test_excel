GET http://localhost:8000/api/v1/cells/

[
    {
        "column": "A",
        "row": 1,
        "value": "315"
    },
    {
        "column": "B",
        "row": 2,
        "value": "45"
    },``
    {
        "column": "A",
        "row": 2,
        "value": "555"
    },
    {
        "column": "C",
        "row": 4,
        "value": "ddd"
    }
]


POST  http://localhost:8000/api/v1/cells/

{"column":"A","row":6,"value":"1"}

DELETE http://localhost:8000/api/v1/cells/{id}

