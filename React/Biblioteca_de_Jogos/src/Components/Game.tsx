type Props = {
  title: string;
  cover: string;
  onRemov: () => void;
};

export default function Game({ title, cover, onRemov }: Props) {
  return (
    <div>
      <img src={cover} alt={title} title={title}></img>
      <div>
        <h2>{title}</h2>
        <button onClick={onRemov}>Remover</button>
      </div>
    </div>
  );
}
