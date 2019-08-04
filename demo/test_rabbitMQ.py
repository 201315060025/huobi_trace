# coding: utf-8
"""
学习 rebbitmq的使用
"""
import pika

def producer_1():
    """"""
    # 创建证书
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('10.150.144.15', 15672, '/', credentials))
    channel = connection.channel()
    # 创建队列 queue
    channel.queue_delcar(queue='blx_test_queue')
    # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channel.asic_publish(exchange='',  routing_key='blx_test_queue', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    producer_1()


