const Modal = ({ active, setActive,children,styleProp}) => {
 
    return (
        <div className={`modal ${active}`}>
            <div className="overlay" onClick={() => setActive(false)}>
                <div style={styleProp} className="modal__inner" onClick={(e) => e.stopPropagation()}>
                    {children}
                </div>
            </div>
        </div>
    );
};

export default Modal;