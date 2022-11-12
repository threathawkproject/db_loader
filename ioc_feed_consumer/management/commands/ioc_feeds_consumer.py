from django.core.management.base import BaseCommand
from ioc_feed_consumer.consumer import KafkaConsumerWrapper
import ioc_feed_consumer.utils




class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f"ready to consume!!")
        # using the Kafka singleton instance
        consumer = KafkaConsumerWrapper.instance()
        for ioc in consumer:
            print(ioc.value)
            ioc_feed_consumer.utils.is_added(ioc.value)
