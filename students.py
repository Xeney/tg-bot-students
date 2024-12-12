class Students():
    students = set()
    
    def create(self, name):
        if name in self.students:
            raise Exception('Студент уже есть')
        self.students.add(name)
        return f"Создан студент \"{name}\""
    
    def delete(self, name):
        if name not in self.students:
            raise Exception('Студент не найден')
        self.students.remove(name)
        return f"Удален студент \"{name}\""
        
