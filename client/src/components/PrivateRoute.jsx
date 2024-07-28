import { Route, Navigate } from 'react-router-dom';
import PropTypes from 'prop-types';

const PrivateRoute = ({ element: Component, ...rest }) => {
    const isAuthenticated = !!localStorage.getItem('accessToken');

    return (
        <Route
            {...rest}
            element={isAuthenticated ? Component : <Navigate to="/login" />}
        />
    );
};

PrivateRoute.propTypes = {
    element: PropTypes.elementType.isRequired,
};

export default PrivateRoute;
