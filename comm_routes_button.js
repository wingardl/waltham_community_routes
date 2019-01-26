'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
       window.location.href = "community_routes.html";
      // return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Community Routes'
    );
  }
}
const domContainer = document.querySelector('#comm_routes_button_container');
ReactDOM.render(e(LikeButton), domContainer);
