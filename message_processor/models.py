from django.db import models

class Message(models.Model):
    asset_id = models.CharField(max_length=100)
    attribute_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=255)  # This will store the processed value

    @classmethod
    def from_json(cls, json_str: str):
        import json
        from datetime import datetime
        data = json.loads(json_str)
        print("debug-----------------------")
        return cls(
            asset_id=data['asset_id'],
            attribute_id=data['attribute_id'],
            timestamp=datetime.fromisoformat(data['timestamp']),
            value=data['value']
        )

