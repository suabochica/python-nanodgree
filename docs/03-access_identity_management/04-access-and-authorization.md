# Access and Authorization

We don't want to give sensitive data to each individual person and some actions are only limited to specific people. In this lesson, we will be adding additional steps to our digital system to check if users have been authorized to perform certain actions.

Authorization answers the question of what can an individual do now that we know who they are. In this lesson, we will focus on what happens after we have verified the identity with a particular service. We will ask one more question: can that individual perform the desired action? Throughout this course, we will implement this using Auth0.

We will cover the following topics:

- Role-permission based access
- Defining roles in Auth0
- Using RBAC in Flask
- Restricting features in frontend

## Role-Permission based Access

With authorization, our goal is to restrict particular people from performing particular actions. This is done by permissions. Permissions are representations of performing a specific action. Generally, permissions consist of an action and a noun such as {get: item}. Permission should be finite and kept as tight as possible and will apply directly to particular tasks that occur within the system.

Users generally fall into a specific category called role. Roles are assigned based on need and permissions are assigned to roles to limit actions to a particular type of user.

After authenticating the user with the authentication service, a token is returned. This token can now include a permission object. This permission is linked to the role assigned to the user. This token is then passed from the frontend to the server to be validated. Once we complete the validation step, we can unpack the token and perform a check to see if the requested action exists within the user's permission object. If the requested action indeed exists, we can return the user's request but if not, we abort the action.

## Defining Rules in Auth0

In Auth0, you can define all the permissions that the API uses. Note that the permissions are heavily dependent on the actions that your API will be fulfilling and you should be careful about assigning each endpoint its own permission.

You can create roles and assign permissions to roles as well as manually assign a role to active users.

## Restricting Feature in the frontend

After the token is passed to the frontend, we can decode the JWT and make use of the payload to render specific features within the frontend. It's important to remember that this doesn't add any security, however, it can help improve user experiece.

## Recap

In this lesson, we discussed the role-based access control design pattern. Following are a list of topics we covered.

- Role-permission based access
- Defining roles in Auth0
- Using RBAC in Flask
- Restricting features in frontend

