const Title = ({icon,children,onClick,className}) => {
    return ( 
        <div className={`title_block ${className}`} onClick={onClick}>
            <span className="title_block__icon">{icon}</span>
            <h1 className="title_block__title">{children}</h1>
        </div>
     );
}
 
export default Title;