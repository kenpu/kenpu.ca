import scala.actors.Actor
import scala.actors.Actor._

actor {
    for(i <- 1 to 10) {
        println(s"Hello ${i}")
        Thread.sleep(1000)
    } 
}

actor {
    for(i <- 1 to 10) {
        println(s"World ${i}")
        Thread.sleep(1000)
    }
}
