use actix_web::{
    get, http::StatusCode, post, web, web::Json, App, HttpResponse, HttpServer, Responder, Result,
};
use serde::{Deserialize, Serialize};
use serde_json::from_str;
use serde_json::Value;

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello There.")
}

//  1. Implement a Flask backend service that tells whether a number received as a parameter is a
//     prime number or not. Use the prior prime number exercise as a starting point. For example, a
//     GET request for number 31 is given as: `http://127.0.0.1:5000/prime_number/31`. The response
//     must be in the format of `{"Number":31, "isPrime":true}`.

#[get("prime_number/{number}")]
// async fn prime_number(path: web::Path<u64>) -> HttpResponse {
async fn prime_number(path: web::Path<u64>) -> Result<String> {
    let number = path.into_inner();
    // HttpResponse::Ok().json(json!({"answer": number}))
    // HttpResponse::Ok().body( format!("{\"Number\":{}, \"isPrime\":{:?}", number ,is_prime(number)) )
    Ok(format!(
        "{{\"Number\":{}, \"isPrime\":{:?}}}",
        number,
        // is_prime(number)
        is_prime_but_working(number)
    ))
    // Ok(format!("number is: {}", if is_prime(number) {"Prime"} else {"Not Prime"}))
}

// 2. Implement a backend service that gets the ICAO code of an airport and then returns the name
//    and location of the airport in JSON format. The information is fetched from the airport
//    database used on this course. For example, the GET request for EFHK would be:
//    `http://127.0.0.1:5000/airport/EFHK`. The response must be in the format of: `{"ICAO":"EFHK",
//    "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}`.

#[derive(Debug, Serialize, Deserialize)]
pub struct Airport {
    icao: String,
    name: String,
    location: String,
}
use sqlx::PgPool;

async fn test_db() -> Result<(), sqlx::Error> {
    let pool = PgPool::connect("mariadb://db_user:thereisaspoon@localhost/test").await?;
    dbg!(pool);
    Ok(())
}

#[get("airport/{icao}")]
async fn get_airport(path: web::Path<String>) -> Result<String> {
    let pool = PgPool::connect("mysql://db_user:thereisaspoon@localhost/test").await;
    dbg!(pool);
    let icao = path.into_inner();
    Ok(format!("GOT: {}", icao))
}

impl Airport {
    //     pub fn new(icao: String, name: String, location: String) -> Self { Self { icao, name, location } }
    pub async fn get_by_icao(icao: &str) -> Result<Airport> {
        // let answer;
        unimplemented!()
    }
}

// async fn get_airport(web::Path(icao): web::Path<String>) -> web::Json<Airport> {
//     let airport = match Airport::get_by_icao(icao) {
//         Some(airport) => airport,
//         None => {
//             return web::Json(Airport {
//                 icao: "".to_string(),
//                 name: "".to_string(),
//                 location: "".to_string(),
//             })
//         }
//     };

//     web::Json(airport)
// }

fn is_prime(n: u64) -> bool {
    if n <= 1 {
        return false;
    }
    if n <= 3 {
        return true;
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false;
    }
    for _i in (5..((n as f64).powf(0.5) + 1.0) as isize).step_by(6) {
        return false;
    }
    return true;
}

fn is_prime_but_working(n: u64) -> bool {
    // if n == 0 or n == 1 {return false}
    for i in 2..n {
        if n % i == 0 {
            return false;
        }
    }
    true
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let data = test_db().await.unwrap();
    dbg!(data);
    HttpServer::new(|| App::new().service(hello).service(prime_number))
        .bind("127.0.0.1:5001")
        .unwrap()
        .run()
        .await
}
