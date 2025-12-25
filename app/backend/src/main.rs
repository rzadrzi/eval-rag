// Response: POST user query and return answer
// Response: GET EvalRAG 

use actix_web::{get, web, App, HttpResponse, HttpServer, Responder, HttpRequest, Result as ActixResult};
use reqwest;
use serde::Deserialize;

#[derive(Deserialize)]
struct QueryParams{
    q: String,
}

#[get("/")]
async fn index( web::Query(params): web::Query<QueryParams>,
    req: HttpRequest,) -> ActixResult<impl Responder> {
    
    let url = reqwest::Url::parse_with_params(
        "http://0.0.0.0:8000/api/query",
        &[("q", &params.q)],
    )
    .map_err(|e| actix_web::error::ErrorBadRequest(e))?;

    let client = reqwest::Client::new();
    let resp = client
        .get(url)
        .send()
        .await
        .map_err(|e| actix_web::error::ErrorBadGateway(e))?;

    let body = resp.text().await.map_err(|e| actix_web::error::ErrorBadGateway(e))?;

    Ok(HttpResponse::Ok().body(body))
}


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}