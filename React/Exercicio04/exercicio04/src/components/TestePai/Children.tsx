type Props = {
  onData: (data: string) => void;
};

export const Children = ({ onData }: Props) => {
  const handleClick = () => {
    const data = "Dados do componente filho";
    onData(data); // Chame a função passada como prop para enviar dados ao componente pai
  };
  return (
    <>
      return (<button onClick={handleClick}>Enviar Dados</button>
      );
    </>
  );
};
