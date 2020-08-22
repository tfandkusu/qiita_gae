package com.tfandkusu.qiitagae

import io.ktor.application.Application
import io.ktor.application.call
import io.ktor.html.respondHtml
import io.ktor.routing.get
import io.ktor.routing.routing
import kotlinx.html.body
import kotlinx.html.head
import kotlinx.html.p
import kotlinx.html.title

fun Application.main() {
    routing {
        get("/") {
            call.respondHtml {
                head {
                    title { +"Hello World" }
                }
                body {
                    p {
                        +"Hello World"
                    }
                }
            }
        }
    }
}
