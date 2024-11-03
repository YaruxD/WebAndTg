export default function Card({ type, product, photo, price, description, state, amount }) {
    return (
        <div className="w-[320px] h-[320px]">
        <a href="vk.com" class="card">
                <img src="https://avatars.mds.yandex.net/i?id=cc9db8ef4e3a64a4d5fe4eebdba8ecf5e35d64a9-9086612-images-thumbs&n=13" class="card__image" alt="" />
            <div class="card__overlay">
                <div class="card__header">
                    <svg class="card__arc" xmlns="http://www.w3.org/2000/svg"><path /></svg>
                    <img class="card__thumb" src="https://i.imgur.com/7D7I6dI.png" alt="" />
                        <div class="card__header-text">
                            <h3 class="card__title">{product}</h3>
                            <span class="card__status">{state} { amount } רע.</span>
                    </div>
                </div>
                    <p class="card__description">{ description }</p>
            </div>
        </a> 
        </div>
    )
}