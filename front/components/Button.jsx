export default function Button({ type, onClick, children }) {
    return (
            <button type={type ?? "button"} onClick={onClick}>{children}</button>
    );
}