import Game from "./Components/Game";
import NewGameForm from "./Components/NewGameForm";
import Hooks from "./Hooks/Hooks";
interface Game {
  id: number;
  title: string;
  cover: string;
}

export default function App() {
  const { addGame, removeGame, games } = Hooks();
  return (
    <div id="app">
      <h1>Biblioteca de Jogos</h1>
      <NewGameForm addGame={addGame}></NewGameForm>
      <div className="games">
        {games.length > 0 ? (
          games.map((game: Game) => {
            return (
              <Game
                key={game.id}
                title={game.title}
                cover={game.cover}
                onRemov={() => removeGame(game.id)}
              ></Game>
            );
          })
        ) : (
          <h2>Não temos nada para exibir</h2>
        )}
      </div>
    </div>
  );
}
