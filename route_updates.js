'use strict';

const crb = React.createElement;

class CommButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      color: '#dfdfdf', };



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
const crbDomContainer = document.querySelector('#route_updates_button_container');
ReactDOM.render(crb(CommButton), crbDomContainer);
