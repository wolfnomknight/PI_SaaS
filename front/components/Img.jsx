const url = (name) => {
    const path = new URL(`/static/${name}.svg`, import.meta.url).pathname;
    return import.meta.env.MODE === 'production' ? `static${path}` : path;
}

export default function Img({ name }) {
    return (
        <img src={url(name)} alt={name} />
    );
}