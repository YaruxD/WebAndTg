export default function Card({ type, product, photo, price, description, state, amount }) {
    return (
        <div className="w-[320px] h-[320px]">
        <a href="vk.com" class="card">
                <img src={photo} class="card__image" alt="" />
            <div class="card__overlay">
                <div class="card__header">
                    <svg class="card__arc" xmlns="http://www.w3.org/2000/svg"><path /></svg>
                    <img class="card__thumb" src="https://i.imgur.com/7D7I6dI.png" alt="" />
                        <div class="card__header-text">
                            <h3 class="card__title">{product}</h3>
                            <span class="card__status">{price}$</span>
                    </div>
                </div>
                    <p class="card__description">{ description }</p>
            </div>  
        </a> 
        </div>
    )
}