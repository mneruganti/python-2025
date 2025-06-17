class contact:
    
    # Initialize a Contact object with a first and last name, phone number, and relationship to the contact
    def __init__(self, name, phone, relationship):
        self.name = name
        self.phone = phone
        self.relationship = relationship
    
    # Return the contact in this form
    def __str__(self):
        return (f"Name: {self.name}\nPhone: {self.phone}\nRelationship: {self.relationship}\n")
    
    # convert data into a dictionary for easy access
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'relationship': self.relationship
        }
    
    # return data given in the form of a dict by using class method
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            phone=data.get('phone'),
            relationship=data.get('relationship')
        )