
module DashHandsontable
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.1.1"

include("jl/''_hottable.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_handsontable",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_handsontable.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_handsontable.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
