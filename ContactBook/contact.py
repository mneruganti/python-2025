class contact:
    
    # Initialize a Contact object with a first and last name, phone number, and relationship to the contact
    def __init__(self, name, phone, relationship):
        self.name = name
        self.phone = phone
        self.relationship = relationship
    
    # Return the contact in this form
    def __str__(self):
        return (f"Name: {self.name}\nPhone: {self.phone}\nRelationship: {self.relationship}\n")
    
    # getters and setters for name, phone, and relationship
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, phone):
        if phone < 0 or len(str(phone)) < 10:
            return "Invalid Phone Number"
        self.phone = phone
    
    @property
    def relationship(self):
        return self.relationship
    
    @relationship.setter
    def relationship(self, relationship):
        self.relationship = relationship
    
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'relationship': self.relationship
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            phone=data.get('phone'),
            relationship=data.get('relationship')
        )