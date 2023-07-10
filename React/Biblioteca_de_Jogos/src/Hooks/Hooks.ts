import { useState } from "react";
interface Game {
  id: number;
  title: string;
  cover: string;
}
export default function Hooks() {
  const [games, setGames] = useState<string[]>(() => {
    const storedGames: string | null = localStorage.getItem("obc-game-lib");
    if (!storedGames) return [];
    return JSON.parse(storedGames);
  });
  const addGame = ({
    title,
    cover,
  }: {
    title: string;
    cover: string;
  }): void => {
    const id = Math.floor(Math.random() * 10000);
    const game: Game = { id, title, cover };
    setGames((state) => {
      //Salvando na state game
      const newState = [...state, game];
      //Salvando no storage
      localStorage.setItem("obc-game-lib", JSON.stringify(newState));
      return newState;
    });
  };

  const removeGame = (id: number) => {
    setGames((state) => {
      //Filtrando os ids que são diferentes do id selecionado e retornando-os
      const newState = state.filter((game) => game.id !== id);
      localStorage.setItem("obc-game-lib", JSON.stringify(newState));
      return newState;
    });
  };

  return { addGame, removeGame, games };
}
