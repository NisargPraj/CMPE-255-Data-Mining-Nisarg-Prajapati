from django.test import TestCase
from .models import Task
from django.urls import reverse


# Create your tests here.

class TaskModelTest(TestCase):
    
    def setUp(self):
        Task.objects.delete()
        
        Task.objects.create(title="Test Task", 
                            description="This is a test task", 
                            completed=False)

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.completed, False)
    
    def test_task_str(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(str(task), "Test Task - This is a test task")
    

class TaskViewTest(TestCase):
    
    def setUp(self):
        Task.objects.create(title="Task 1", 
                            description="This is a test task 1", 
                            completed=True)
        Task.objects.create(title="Task 2", 
                            description="This is a test task 2", 
                            completed=False)
        
    def test_index_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')
 
    
class TaskAddViewTest(TestCase):
    
    def test_add_task_view(self):
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_task.html')
        
        response = self.client.post(reverse('add_task'), 
                                    {'title': 'New Task', 
                                     'description': 'This is a new task'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        
        new_task = Task.objects.first()
        
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, new_task.title)
        self.assertContains(response, new_task.description)
        self.assertContains(response, new_task.completed)
        

class TaskCompleteViewTest(TestCase):
        
        def test_complete_task_view(self):
            Task.objects.delete()
            
            task = Task.objects.create(title="Task 1", 
                                    description="This is a test task 1", 
                                    completed=False)
            
            response = self.client.get(reverse('complete_task'), 
                                    {'task_id': str(task._id)})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('task_list'))
            
            task = Task.objects.get(_id=task._id)
            self.assertEqual(task.completed, True)
            self.assertIsNotNone(task.completed_at)


class TaskDeleteViewTest(TestCase):
        
        def test_delete_task_view(self):
            task = Task.objects.create(title="Task 1", 
                                        description="This is a test task 1", 
                                        completed=False)
            
            response = self.client.get(reverse('delete_task'), 
                                        {'task_id': str(task._id)})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('task_list'))
            
            task = Task.objects(_id=task._id).first()  # Use _id instead of id
            self.assertIsNone(task)