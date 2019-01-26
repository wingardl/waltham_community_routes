'use strict';

const crb = React.createElement;

class CommButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {
    if (this.state.clicked) {
       window.location.href = "route_updates.html";
      // return 'You liked this.';
    }

    return crb(
      'button',
      { onClick: () => this.setState({ clicked: true }) },
      'Route Updates'
    );
  }
}
const crbDomContainer = document.querySelector('#route_updates_button_container');
ReactDOM.render(crb(CommButton), crbDomContainer);
