'use strict';

const rub = React.createElement;

class routeUpdateButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      color: '#000000' };



  }

  render() {
    if (this.state.clicked) {
       window.location.href = "routeupdates.html";
      // return 'You liked this.';
    }

    return rub(
      'button',
      { onClick: () => this.setState({ clicked: true }) },
      'Route Updates'
    );
  }
}
const routeUpdateDomContainer = document.querySelector('#route_updates_button_container');
ReactDOM.render(rub(routeUpdateButton), routeUpdateDomContainer);
