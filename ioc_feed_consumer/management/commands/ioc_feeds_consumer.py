from django.core.management.base import BaseCommand
from ioc_feed_consumer.consumer import KafkaConsumerWrapper
import ioc_feed_consumer.utils
 


# This is the job that runs consumer which ingests the IOC and checks for the following
# 1. Is Added if so update it!
# 2. Is not add it in our DB
class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f"ready to consume!!")
        # using the Kafka singleton instance
        consumer = KafkaConsumerWrapper.instance()
        for ioc in consumer:
            # checking if the ioc exists in our db
            is_added = ioc_feed_consumer.utils.is_added(ioc.value)
            if is_added:
                # update it!
                ioc_feed_consumer.utils.update(ioc)
            else:
                # add it!
                ioc_feed_consumer.utils.add(ioc)
        
