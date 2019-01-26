'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
       window.location.href = "route_updates.html";
      // return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Route Updates'
    );
  }
}
const domContainer = document.querySelector('#route_updates_button_container');
ReactDOM.render(e(LikeButton), domContainer);
