import { useState } from "react";
import TextInput from "./TextInput";
type Props = {
  addGame: (game: { title: string; cover: string }) => void;
};
export default function NewGameForm({ addGame }: Props) {
  const [title, setTitle] = useState<string>("");
  const [cover, setCover] = useState<string>("");
  const handleSubmit = (ev: React.FormEvent<HTMLFormElement>): void => {
    ev.preventDefault();
    addGame({ title, cover });
    setTitle("");
    setCover("");
  };
  return (
    <form onSubmit={handleSubmit}>
      <TextInput
        id="title"
        label="Título:"
        value={title}
        setValue={setTitle}
      ></TextInput>
      <TextInput
        id="cover"
        label="Capa:"
        value={cover}
        setValue={setCover}
      ></TextInput>

      <button type="submit">Adicionar à biblioteca</button>
    </form>
  );
}
