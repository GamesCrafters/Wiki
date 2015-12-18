Server\_Workflow
================

Initialization workflow:

------------------------------------------------------------------------

1) Read config file for IModule implemenation class names. 2) foreach name in config file

`       instantiate IModule implemenation and add to modulesArray`

Request workflow:

------------------------------------------------------------------------

1) HTTP requests come into the GMServlet 2) GMServlet reads all headers and creates a IModuleRequest and IModuleResponse object from

`   the HttpServletRequest and HttpServletResponse (and read request headers).`

3) foreach IModule module in modulesArray

`       if (module.typeSupported(typeHeaderVal))`
`           module.handleRequest(req, res)`
`  handleError(req, res, errorCode);`
