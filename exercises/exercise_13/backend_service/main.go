// 1. Implement a Flask backend service that tells whether a
// number received as a parameter is a prime number or not. Use
// the prior prime number exercise as a starting point. For
// example, a GET request for number 31 is given as:
// `http://127.0.0.1:5000/prime_number/31`. The response must be
// in the format of `{"Number":31, "isPrime":true}`.

package main

import "github.com/gofiber/fiber/v2"

func main() {
  app := fiber.New()

  app.Get("/prime_number/*", func(c *fiber.Ctx) error {
    return c.SendString("Hello, World 👋! {c.path}")
  })

  app.Listen(":5000")
}


// def part3():
//     number = 0
//     try:
//         number = int(input("Throw me some number (int): ").strip())
//     except:
//         print("Input an integer.")
//         return
//
//     def is_prime(n: int) -> bool:
//         if n <= 1:
//             return False
//         if n <= 3:
//             return True
//         if n % 2 == 0 or n % 3 == 0:
//             return False
//         for i in range(5, int(n**0.5) + 1, 6):
//             if n % i == 0 or n % (i + 2) == 0:
//                 return False
//         return True
