import { useState } from "react";
import { Children } from "./Children";
export const Parent = () => {
  const [dataFromChild, setDataFromChild] = useState<string>("");

  const handleDataFromChild = (data: string): void => {
    // Manipule os dados recebidos do componente filho como desejado
    alert("Dados recebidos do componente filho:" + data);
    setDataFromChild(data);
  };

  return (
    <>
      <div>
        <Children onData={handleDataFromChild} />
        <p>Dados recebidos do componente filho: {dataFromChild}</p>
      </div>
    </>
  );
};
