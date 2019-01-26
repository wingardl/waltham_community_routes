'use strict';

const crb = React.createElement;

class Button extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {
    if (this.state.clicked) {
       window.location.href = "community_routes.html";
      // return 'You liked this.';
    }

    return crb(
      'button',
      { onClick: () => this.setState({ clicked: true }) },
      'Community Routes'
    );
  }
}
const domContainer = document.querySelector('#comm_routes_button_container');
ReactDOM.render(crb(Button), domContainer);
