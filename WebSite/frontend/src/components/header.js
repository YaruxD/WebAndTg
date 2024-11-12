import UserIcon from '../images/free-icon-user-profile-14983653.png';
import { Link } from 'react-router-dom';

export default function Header() {
    return (
<>
        <div class="container">
		<ul class="slider-menu">
			<li><Link to='/'>Catalog</Link></li>
			<li>About</li>
			<li>Services</li>
		</ul>
		<ul class="signup-menu">
			<li><Link to='/authorization'><img src={UserIcon} alt=''></img></Link></li>
		</ul>
</div>

		
</>
    )
}