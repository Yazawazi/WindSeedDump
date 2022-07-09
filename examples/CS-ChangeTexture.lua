local function findActiveAvatar()
    local avatarRoot = CS.UnityEngine.GameObject.Find("/EntityRoot/AvatarRoot")
    if avatarRoot.transform.childCount == 0 then
        return
    end
    for i = 0, avatarRoot.transform.childCount - 1 do
        local avatar = avatarRoot.transform:GetChild(i)
        if avatar.gameObject.activeInHierarchy then
            return avatar.gameObject
        end
    end
end

local function findAvatarBody(avatar)
    for i = 0, avatar.transform.childCount - 1 do
        local transform = avatar.transform:GetChild(i)
        if transform.name == "OffsetDummy" then
            for j = 0, transform.childCount - 1 do
                local child = transform:GetChild(j)
                for k = 0, child.transform.childCount - 1 do
                    local body = child.transform:GetChild(k)
                    if body.name == "Body" then
                        return body.gameObject
                    end
                end
            end
        end
    end
end


local function replaceTexture()
    local nowAvatar = findActiveAvatar()
    local nowBody = findAvatarBody(nowAvatar)
    local texture = CS.UnityEngine.Texture2D(2048, 2048)
    local image = CS.System.IO.File.ReadAllBytes("F:/hutao.png")
    CS.UnityEngine.ImageConversion.LoadImage(texture, image)
    local renderer = nowBody:GetComponent(typeof(CS.UnityEngine.SkinnedMeshRenderer))
    renderer.materials[1].mainTexture = texture
    
end

local function onError(error)
    CS.UnityEngine.GameObject.Find("/BetaWatermarkCanvas(Clone)/Panel/TxtUID"):GetComponent("Text").text = tostring(error)
end

xpcall(replaceTexture, onError)
