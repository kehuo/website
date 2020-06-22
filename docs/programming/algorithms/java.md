# Java

![Hierarchy of Java Collection framework](D:\Project\website\docs\assets\img\java-collection-hierarchy.png)

![Java Map Hierarchy](D:\Project\website\docs\assets\img\java-map-hierarchy.png)

|            Thread Unsafe             |              Thread Safe               |
| :----------------------------------: | :------------------------------------: |
|            StringBuilder             |              StringBuffer              |
|              ArrayList               |                 Vector                 |
| HashMap (allow key or value is null) | HashTable (key and value are nullable) |
|                                      |               Properties               |
|       TreeMap (red black tree)       |                                        |
|                                      |         java.util.concurrent.*         |

![author="pat" timestamp="20121117T215954-0600" comment="I think this originally came from the nutshell book. Do they have an update for this diagram that we could use? (Maybe one for NIO?)"The java.io package](D:\Project\website\docs\assets\img\java-io-stream-hierarchy.png)



![图11-4 线程生命周期图.png](D:\Project\website\docs\assets\img\java-thread-states.png)

线程死亡后，不能重新开启，再次开启是一个新的线程。

```javascript [a]
console.log("Hello world!");
```

```python [a]
print('Hello world!')
```

```ruby [a]
puts 'Hello world!'
```
