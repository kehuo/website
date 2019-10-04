/*
* @Author: Lucien Zhang
* @Date:   2019-09-29 18:02:32
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-10-02 12:39:27
*/
var Queue = (()=>{
  const map = new WeakMap();
  let _items = []
  class Queue{
    constructor(...items){
      //initialize the items in queue
      map.set(this, []);
      _items = map.get(this);
      // enqueuing the items passed to the constructor
      this.enqueue(...items)
    }

    enqueue(...items){
      //push items into the queue
      this._items = [...this._items, ...items]
      return this._items;
    }

    dequeue(count=1){
      //pull out the first item from the queue
      _items.splice(0,count);
      return this._items;
    }

    peek(){
      //peek at the first item from the queue
      return _items[0]
    }

    size(){
      //get the length of queue
      return _items.length
    }

    isEmpty(){
      //find whether the queue is empty or no
      return _items.length===0
    }

    toArray(){
      return _items
    }

  }
  return Queue
})()

let audio_status='waiting';


// let my_queue = new Queue(1,24,4);
// // [1, 24, 4]
// my_queue.enqueue(23)
// //[1, 24, 4, 23]
// my_queue.enqueue(1,2,342);
// //[1, 24, 4, 23, 1, 2, 342]
// my_queue.dequeue();
// //[24, 4, 23, 1, 2, 342]
// my_queue.dequeue(3)
// //[1, 2, 342]
// my_queue.isEmpty()
// // false
// my_queue.size();
// //3
// my_queue.toArray();
// //[1, 2, 342]


setInterval(function)
