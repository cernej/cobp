from dataclasses import dataclass,field

@dataclass
class User:
    name: str
    emails: list[str] = field(default_factory=list)


if __name__ == "__main__":
    bob = User("Bob")
    print(bob)
    alice = User("Alice")
    print(alice)

    bob.emails.append("email3")
    alice.emails.append("email4")
    print(bob)
    print(alice)