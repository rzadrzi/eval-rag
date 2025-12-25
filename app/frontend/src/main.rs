use yew::prelude::*;

#[component]
fn App() -> Html {
    // html! {
    //     <h1>{ "Hello World" }</h1>
    // }

    html! {
        <>

        <h1>{"Hello, world!"}</h1>
        <section style="background-color: #eee;">
            <div class="container py-5">
                <div class="row d-flex justify-content-center">
                    <div class="col-md-8 col-lg-6 col-xl-4">
                        <div class="card" id="chat1" style="border-radius: 15px;">

                        
                        </div>
                    </div>
                </div>
            </div>
        </section>

        </>
  }
}

fn main() {
    yew::Renderer::<App>::new().render();
}