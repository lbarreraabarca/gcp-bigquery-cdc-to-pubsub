
class RequestParser():
    def __init__(self, data: dict) -> None:
        self._data = data

    def get_method_name(self) -> str:
        return self.data["protoPayload"]["methodName"]

    def get_job_id(self) -> str:
        job_id = self.data["protoPayload"]["metadata"]["tableDataChange"]["jobName"]
        job_splitted = job_id.split("/")
        return job_splitted[len(job_splitted)-1]

    def get_resource_specs(self):
        resource_splitted = str(self.data["protoPayload"]["resourceName"]) \
            .split("/")
        return resource_splitted[1], resource_splitted[3], resource_splitted[5]

    @property
    def data(self) -> dict:
        return self._data
