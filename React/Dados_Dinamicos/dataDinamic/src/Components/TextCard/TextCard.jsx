import * as C from "./StyleTextCard";
import { Button } from "../Button/StyledButton";
export const TextCard = ({ title, poster }) => {
  return (
    <>
      <C.Container>
        <C.ContentCard>
          <div>
            <img
              style={{ boxShadow: "0 2px 4px rgba(0, 0, 0, 0.5)" }}
              src={poster}
              alt={title}
              width="220px"
            ></img>
          </div>

          <C.AreaText>
            <C.Title>{title}</C.Title>
            <C.Description>
              A princesa Leia é mantida refém pelas forças imperiais comandadas
              por Darth Vader. Luke Skywalker e o capitão Han Solo precisam
              libertá-la e restaurar a liberdade e a justiça na galáxia.
            </C.Description>
            <Button>Comprar Agora</Button>
          </C.AreaText>
        </C.ContentCard>
      </C.Container>
    </>
  );
};
