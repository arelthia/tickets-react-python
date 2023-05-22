import Footing from "./components/Footing";
import Heading from "./components/Heading";
import Main from "./components/Main";
import "../src/App.css"
import TicketList from "./components/TicketList";



function App() {
  return (
    <div className="wrapper">
      <Heading title="Support Dashboard"/>
      <Main>
        <TicketList />
      </Main>
      <Footing />
    </div>
    
  );
}

export default App;
