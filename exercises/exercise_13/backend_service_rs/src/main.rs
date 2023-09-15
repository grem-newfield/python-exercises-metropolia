use actix_web::body::EitherBody;
use actix_web::HttpRequest;
use actix_web::{get, web, App, HttpResponse, HttpServer, Responder, Result};
use is_prime::is_prime;
use mysql::prelude::Queryable;
use mysql::Pool;
use serde::{Deserialize, Serialize};

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello There.")
}

//  1. Implement a Flask backend service that tells whether a number received as a parameter is a
//     prime number or not. Use the prior prime number exercise as a starting point. For example, a
//     GET request for number 31 is given as: `http://127.0.0.1:5000/prime_number/31`. The response
//     must be in the format of `{"Number":31, "isPrime":true}`.

#[get("prime_number/{number}")]
async fn prime_number(path: web::Path<String>) -> Result<String> {
    let number = path.into_inner();
    Ok(format!(
        "{{\"Number\":{}, \"isPrime\":{:?}}}",
        number,
        is_prime(&number)
    ))
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

impl Airport {
    pub fn new(icao: String, name: String, location: String) -> Self {
        Self {
            icao,
            name,
            location,
        }
    }
}

#[get("airport/{icao}")]
async fn get_airport(
    req: HttpRequest,
    path: web::Path<String>,
) -> HttpResponse<EitherBody<String>> {
    let icao = path.into_inner();
    let mut conn = Pool::new("mysql://db_user:thereisaspoon@localhost/test")
        .unwrap()
        .get_conn()
        .unwrap();
    let sql = format!(
        "SELECT ident, name, municipality FROM airport WHERE ident = \"{}\"",
        icao.to_uppercase()
    );
    dbg!(&sql);
    let result: (String, String, String) = match conn.query_first(sql).unwrap() {
        Some(data) => data,
        None => (
            "Undefined".to_string(),
            "Undefined".to_string(),
            "Undefined".to_string(),
        ),
    };

    let body = web::Json(Airport {
        icao: result.0,
        name: result.1,
        location: result.2,
    });

    dbg!(&body);
    let res = body.respond_to(&req);
    res
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(prime_number)
            .service(get_airport)
    })
    .bind("127.0.0.1:5000")
    .unwrap()
    .run()
    .await
}
