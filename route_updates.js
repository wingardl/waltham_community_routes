'use strict';

const e = React.createElement;

class Button extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {

    if (this.state.clicked) {
       window.location.href = "route_updates.html";
      // return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ clicked: true }) },
      'Route Updates'
    );
  }
}
const domContainer = document.querySelector('#route_updates_button_container');
ReactDOM.render(e(Button), domContainer);
