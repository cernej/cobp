from dataclasses import dataclass, asdict, astuple
import json
import pickle
from user_pb2 import User
from pydantic import BaseModel, ValidationError

@dataclass
class DUser:
    name: str
    age: int

class PUser(BaseModel):
    name: str
    age: int


if __name__ == "__main__":

    u1 = DUser("Bob", 18)
    u2 = User(name="Bob", age=18)
    u3 = PUser(name="Bob", age="25")

    json_data = json.dumps(astuple(u1))
    print(len(json_data))

    pickle_data = pickle.dumps(u1)
    #print(pickle_data)
    print(len(pickle_data))

    proto_data = u2.SerializeToString()
    #print(proto_data)
    print(len(proto_data))

    py_data = u3.model_dump_json()
    py_data = '{"name": "Bob", "age": "x"}'
    try:
        print(PUser.model_validate_json(py_data))
    except ValidationError as e:
        print(e.errors())


