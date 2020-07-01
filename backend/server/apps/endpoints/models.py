from django.db import models

# Create your models here.
class Endpoint(models.Model):
    '''
        Description:
            Represents an ML API Endpoint.

        Attributes:
            name: The name of the endpoint, it will be used in API URL,
            owner: The string with owner name,
            created_at: The date when the endpoint was created
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
    '''
        Description: 
            Represents the ML algorithm object.

        Attributes:
            name: The name of the algorithm.
            description: The short description of how the algorithm works.
            code: The code of the algorithm.
            version: The version of the algorithm similar to software versioning.

            owner: The name of the owner.
            created_at: The date when the MLAlgorithm was added.
            parent_endpoint: The reference to the endpoint.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner =  models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
    '''
        Description:
            Represents the status of the MLAgorithm which can change over time

        Attributes:
            status: The status of the algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
            active: The boolean flag which point to currently active atatus
            created_by: The name of the creator.
            created_at: The date of status creation.
            parent_mlalgorithm: The reference to corresponding MLAlgorithm. 
    '''

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")

class MLRequest(models.Model):
    '''
        Description:
            This will keep imformation about all requests to the ML algorithms.

        Attributes:
            input_data: The input data to ML algorithm in JSON format.
            full_response: The response of the ML Algorithm.
            response: The response of the ML algorithm in JSOM format.
            feedback: Feedback about the response in JSON format.
            created_at: The date when the request was created.
            parent_mlalgorithm: The reference to MLAlgorithm used to compute response.
    '''

    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)